#=
    For each categories non numerical categories (in head), get:
        1. Missing (already calculated in remove_missing())
        2. Count
        3. Number of different values
        4. Most common value
        5. Number of occurences of the most common value
=#
function describe_non_num(non_num_values, head, describe_non_num_table)
    count = 0
    all_values = Dict()
    for elem in non_num_values[head]
        count += 1
        if haskey(all_values, elem)
            all_values[elem] += 1
        else
            push!(all_values, elem => 1)
        end
    end
    push!(describe_non_num_table[head], count)
    max_key = reduce((x, y) -> all_values[x] >= all_values[y] ? x : y, keys(all_values))
    push!(describe_non_num_table[head], length(keys(all_values)))
    push!(describe_non_num_table[head], describe_non_num_table[head][2] / describe_non_num_table[head][3])
    push!(describe_non_num_table[head], max_key)
    push!(describe_non_num_table[head], all_values[max_key])
end