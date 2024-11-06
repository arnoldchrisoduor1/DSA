defmodule TwoLargest do
  def find_two_largest(list) when length(list) < 2 do
    raise ArgumentError, "List must contain at least two elements"
  end

  def find_two_largest(list) do
    list
    |> Enum.sort()
    |> Enum.take(-2)
  end
end

input = [5, 3, 8, 1, 9, 4]
IO.puts("Input: #{inspect(input)}")

result = TwoLargest.find_two_largest(input)
IO.puts("Result: [#{Enum.join(result, ", ")}]")

IO.puts("First largest: #{Enum.at(result, 0)}")
IO.puts("Second largest: #{Enum.at(result, 1)}")
