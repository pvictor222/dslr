#=
    Removes the missing elements from the array
    Counts the number of missing elements and adds it to describe_table[head]
=#
function remove_missing(numerical_values, head, describe_table)
    missing_elem = []
    for i in 1:length(numerical_values[head])
        if (ismissing(numerical_values[head][i]) == true)
            push!(missing_elem, i)
        end
    end
    count = 0
    for elem in sort(missing_elem, rev=true)
        splice!(numerical_values[head], elem)
        count += 1
    end
    push!(describe_table[head], count)
end
