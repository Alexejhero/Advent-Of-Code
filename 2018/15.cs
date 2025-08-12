// ReSharper disable CheckNamespace, ArrangeTypeModifiers

using System.Diagnostics;
using System.Runtime.CompilerServices;

#pragma warning disable CA2211, CS8509, CS8524

namespace AOC;

public enum Type
{
    Empty,
    Wall,
    Goblin,
    Elf
}

public class Square(Type type, int x, int y)
{
    public Type Type = type;
    public int Health = 200;
    public int Damage = 3;
    public int X = x;
    public int Y = y;
}

public static class Program
{
    public static readonly (int yOffset, int xOffset)[] Directions = [(-1, 0), (0, -1), (0, 1), (1, 0)];

    public static Square[,] Map;

    public static void Log()
    {
        for (int y = 0; y < Map.GetLength(0); y++)
        {
            for (int x = 0; x < Map.GetLength(1); x++)
            {
                Console.Write(Map[y, x].Type switch
                {
                    Type.Empty => '.',
                    Type.Wall => '#',
                    Type.Goblin => 'G',
                    Type.Elf => 'E',
                });
            }

            Console.Write("   ");

            for (int x = 0; x < Map.GetLength(1); x++)
            {
                Console.Write(Map[y, x].Type switch
                {
                    Type.Goblin => $"G({Map[y, x].Health}) ",
                    Type.Elf => $"E({Map[y, x].Health}) ",
                    _ => "",
                });
            }

            Console.WriteLine();
        }
    }

    public static void Main()
    {
        string[] lines = File.ReadAllLines("C:/Users/alexe/Desktop/input.in");
        Map = new Square[lines.Length, lines[0].Length];

        for (int y = 0; y < lines.Length; y++)
        {
            for (int x = 0; x < lines[y].Length; x++)
            {
                Map[y, x] = new Square(lines[y][x] switch
                {
                    '#' => Type.Wall,
                    '.' => Type.Empty,
                    'G' => Type.Goblin,
                    'E' => Type.Elf,
                }, x, y);
            }
        }

        int turn = 0;
        try
        {
            for (turn = 1;; turn++)
            {
                Console.WriteLine("Turn " + turn);
                Round();
                Log();
            }
        }
        catch (EndCombat)
        {
            Console.WriteLine($"Combat ended after {turn - 1} turns");

            int totalHealth = 0;

            foreach (Square unit in Map)
            {
                if (unit.Type >= Type.Goblin) totalHealth += unit.Health;
            }

            Console.WriteLine($"Total health: {totalHealth}");
            Console.WriteLine($"Result: {(turn - 1) * totalHealth}");
        }
    }

    public static void Round()
    {
        List<Square> units = [];

        for (int y = 0; y < Map.GetLength(0); y++)
        {
            for (int x = 0; x < Map.GetLength(1); x++)
            {
                Square unit = Map[y, x];
                if (unit.Type >= Type.Goblin) units.Add(unit);
            }
        }

        // Sort units by their position (reading order)
        units = units.OrderBy(u => u.Y).ThenBy(u => u.X).ToList();

        foreach (Square unit in units)
        {
            if (unit.Type >= Type.Goblin)
            {
                Turn(units, unit);
            }
        }
    }

    [MethodImpl(MethodImplOptions.AggressiveInlining)]
    public static void Turn(List<Square> allUnits, Square myself)
    {
        // Find all enemy units
        Square[] enemyUnits = allUnits.Where(s => s.Type != myself.Type).ToArray();
        // If no enemy units remain, combat ends
        if (enemyUnits.Length == 0) throw new EndCombat();

        // Find all open squares around enemies
        List<Square> enemyUnitsThatICanAttack = [];
        List<Square> emptySquaresInRangeOfEnemies = [];
        foreach (Square enemyUnit in enemyUnits)
        {
            foreach ((int yOffset, int xOffset) in Directions)
            {
                Square spaceAdjecentToEnemy = Map[enemyUnit.Y + yOffset, enemyUnit.X + xOffset];
                if (spaceAdjecentToEnemy == myself) enemyUnitsThatICanAttack.Add(enemyUnit);
                if (spaceAdjecentToEnemy.Type == Type.Empty) emptySquaresInRangeOfEnemies.Add(spaceAdjecentToEnemy);
            }
        }

        // End turn if we are not in range and we cannot get in range
        if (emptySquaresInRangeOfEnemies.Count == 0 && enemyUnitsThatICanAttack.Count == 0) return;

        if (enemyUnitsThatICanAttack.Count > 0) Attack(myself, enemyUnitsThatICanAttack);
        else Move(myself, emptySquaresInRangeOfEnemies, enemyUnits);
    }

    public static void Move(Square myself, List<Square> possibleDestinations, Square[] enemyUnits)
    {
        // Find closest square that is in range of a target
        Queue<(Square square, int distance, Square? previous)> queue = new();
        HashSet<Square> visited = new();
        queue.Enqueue((myself, 0, null));
        visited.Add(myself);

        Square? closestSquare = null;
        int minDistance = int.MaxValue;
        Square? nextStep = null;

        while (queue.Count > 0)
        {
            var (current, distance, previous) = queue.Dequeue();

            if (possibleDestinations.Contains(current))
            {
                if (distance < minDistance || (distance == minDistance && possibleDestinations.IndexOf(current) < possibleDestinations.IndexOf(closestSquare)))
                {
                    closestSquare = current;
                    minDistance = distance;
                    nextStep = previous;
                }
            }

            foreach (var (yOffset, xOffset) in Directions)
            {
                int newY = current.Y + yOffset;
                int newX = current.X + xOffset;

                if (newY >= 0 && newY < Map.GetLength(0) && newX >= 0 && newX < Map.GetLength(1))
                {
                    Square neighbor = Map[newY, newX];
                    if (neighbor.Type == Type.Empty && !visited.Contains(neighbor))
                    {
                        queue.Enqueue((neighbor, distance + 1, previous == null ? neighbor : previous));
                        visited.Add(neighbor);
                    }
                }
            }
        }

        // If there is no such square, return
        if (closestSquare == null) return;

        // Move towards the closestSquare
        if (nextStep != null)
        {
            Map[myself.Y, myself.X] = new Square(Type.Empty, myself.X, myself.Y);
            myself.X = nextStep.X;
            myself.Y = nextStep.Y;
            Map[myself.Y, myself.X] = myself;
        }

        // Then attack
        List<Square> enemyUnitsThatICanAttack = [];
        foreach (Square enemyUnit in enemyUnits)
        {
            foreach ((int yOffset, int xOffset) in Directions)
            {
                Square spaceAdjecentToEnemy = Map[enemyUnit.Y + yOffset, enemyUnit.X + xOffset];
                if (spaceAdjecentToEnemy == myself) enemyUnitsThatICanAttack.Add(enemyUnit);
            }
        }
        Attack(myself, enemyUnitsThatICanAttack);
    }

    public static void Attack(Square myself, List<Square> enemyUnits)
    {
        // Select closest enemy that has the least amount of health, reading order is tiebreaker
        Square chosenEnemy = enemyUnits.OrderBy(e => e.Health)
            .ThenBy(e => e.Y)
            .ThenBy(e => e.X)
            .FirstOrDefault();

        if (chosenEnemy == null) return;
        if (myself.Type < Type.Goblin) return;

        chosenEnemy.Health -= myself.Damage;
        if (chosenEnemy.Health <= 0)
        {
            if (Map[chosenEnemy.Y, chosenEnemy.X] != chosenEnemy) throw new UnreachableException();
            chosenEnemy.Type = Type.Empty;
        }
    }
}

public class EndCombat : Exception;