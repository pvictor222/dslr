#=
    Returns the standard deviation of the array
    Standard deviation = square root of (1/n * sum of each (element - mean)^2)
=#
function standard_deviation(mean, values_array)
    value = 0
    for elem in values_array
        value += (elem - mean)^2
    end
    return ((value / length(values_array))^1/2)
end