using CSV

include("src_histogram/print_histogram.jl")
include("src_histogram/remove_missing_rows.jl")
include("src_describe/describe_non_num.jl")

#=
    1. Read the data from CSV
    2. Get the numerical headers and numerical values
    3. Print_histogram() to actualy plot the data
=#
if (length(ARGS) < 1 || ARGS[1] == "")
    println("Please add an argument")
elseif (isfile(ARGS[1]) && length(ARGS[1]) > 5 && lowercase(SubString(ARGS[1], length(ARGS[1]) - 3, length(ARGS[1]))) == ".csv")
    csv_file = CSV.read(ARGS[1])
    headers = [header for header in split(readline(ARGS[1]), ',')]
    filter!(head -> head ≠ "Index", headers)
    numerical_headers = []
    numerical_values = Dict()
    houses = unique(csv_file["Hogwarts House"])
    for head in headers
        if (typeof(csv_file[head][2]) == Float64 || typeof(csv_file[head][2]) == Int64)
            push!(numerical_headers, head)
            numerical_values[head] = [elem for elem in csv_file[head]]
        end
    end
    house_values = [elem for elem in csv_file["Hogwarts House"]]
    remove_missing_rows(numerical_values, house_values, numerical_headers)
    print_histogram(numerical_headers, numerical_values, houses, house_values)

else
    println("The file does not exist or is not a CSV file")
end