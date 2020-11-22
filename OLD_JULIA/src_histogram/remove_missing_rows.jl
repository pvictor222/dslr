#=
    Removes the entire row if one value is missing
=#
function remove_missing_rows(numerical_values, house_values, numerical_headers)
    i = 0
    println(length(house_values))
    for elem in 0:length(house_values)
        println(i)
        i += 1;
    end
    println("i = $i")
end