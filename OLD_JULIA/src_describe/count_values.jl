#=
    Returns the number of elements of the array
=#
function count_values(values_array)
    value = 0
    for elem in values_array
        value += 1
    end
    return (value)
end