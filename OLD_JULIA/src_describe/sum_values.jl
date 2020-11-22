#=
    Returns the sum of the elements of the array
=#
function sum_values(values_array)
    value = 0
    for elem in values_array
        value += elem
    end
    return (value)
end