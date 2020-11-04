using CSV
using TypedTables

include("src_describe/describe_values.jl")
include("src_describe/remove_missing.jl")

#=
    1. Check that the file exists and it's a .csv file
    2. Put all the numerical headers in the array "numerical_headers"
    3. Put all the numerical values in the dictionnary "numerical_values(numerical_headers => [values])"
    4. Remove missing values
    5. Send 

TODO
- mean
- std
- min
- Q1
- Q2 
- Q3 
- max
- number of missing values (bonus)
- print the type
- clean the code with more functions in the main
- Use excel to check that  all is correct

=#
if (length(ARGS) < 1 || ARGS[1] == "")
    println("Please add an argument")
elseif (isfile(ARGS[1]) && length(ARGS[1]) > 5 && lowercase(SubString(ARGS[1], length(ARGS[1]) - 3, length(ARGS[1]))) == ".csv")
    csv_file = CSV.read(ARGS[1])
    headers = [header for header in split(readline(ARGS[1]), ',')]
    filter!(head -> head ≠ "Index", headers)
    numerical_headers = []
    numerical_values = Dict()
    describe_table = Dict()
    for head in headers
        if (typeof(csv_file[head][2]) == Float64 || typeof(csv_file[head][2]) == Int64)
            push!(numerical_headers, head)
            numerical_values[head] = [elem for elem in csv_file[head]]
            describe_table[head] = []
            remove_missing(numerical_values, head, describe_table)
            describe_values(numerical_values, head, describe_table)
        end
    end
    println(describe_table)
else
    println("The file does not exist or is not a CSV file")
end
