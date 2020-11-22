#=
    Returns the max of the array
=#
function max_values(values_array)
    value = -2^7
    for elem in values_array
        if elem > value
            value = elem
        end
    end
    return (value)
end