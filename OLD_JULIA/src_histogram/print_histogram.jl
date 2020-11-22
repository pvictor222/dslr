using Plots, Dates

#=
Documentation for plots in Julia: https://docs.juliaplots.org/latest/tutorial/#Plotting-in-Scripts
    - For all subjects:
        - Dispatch the values between houses
        - Plot the grades of all houses with different colors
    - Combine all plots on one sheet
    - Asks the user if he wants to save it as pdf or png
=#
function print_histogram(headers, numerical_values, houses, house_values)
    println(headers)
    # println(house_values)
    # p1 = histogram(house_values, numerical_values[headers[1]])
    histogram(numerical_values[headers[1]], bins=:scott, weights=repeat(1:5, outer=200))
    println("Do you want to save the plot as PDF of PNG? PDF is by default. (PDF/PNG)")
    format = readline()
    format = (format != "" && lowercase(format) == "png") ? "png" : "pdf"
    savefig("~/Desktop/plot$(Dates.format(now(), "HH:MM:SS")).$format")
    savefig("~/Desktop/plot$(Dates.format(now(), "HH:MM:SS")).$format")

    # for head in headers
    #     values_by_house = separate_values_by_house(, numerical_values, head)
    # end
    # histogram(non_num_values["Hogwarts House"], numerical_values["Arithmancy"])
end