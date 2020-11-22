#=
    Returns the min of the array
=#
function min_values(values_array)
    value = 2^7 - 1
    for elem in values_array
        if elem < value
            value = elem
        end
    end
    return (value)
end