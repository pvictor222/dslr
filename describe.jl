using CSV

include("src_describe/describe_values.jl")
include("src_describe/describe_non_num.jl")
include("src_describe/remove_missing.jl")
include("src_describe/print_table.jl")
include("src_describe/print_non_num_table.jl")

#=
    1. Check that the file exists and it's a .csv file
    2. Put all the numerical headers in the array "numerical_headers"
    3. Put all the numerical values in the dictionnary "numerical_values(numerical_headers => [values])"
    4. Remove missing values
    5. Send describe_values() to get the descriptive data and store it in describe_table
    6. Send to print_table() to get it printed
BONUS:
    - Missing values
    - Description of the other categories
    - Pretty table formatting
=#
if (length(ARGS) < 1 || ARGS[1] == "")
    println("Please add an argument")
elseif (isfile(ARGS[1]) && length(ARGS[1]) > 5 && lowercase(SubString(ARGS[1], length(ARGS[1]) - 3, length(ARGS[1]))) == ".csv")
    csv_file = CSV.read(ARGS[1])
    headers = [header for header in split(readline(ARGS[1]), ',')]
    filter!(head -> head ≠ "Index", headers)
    numerical_headers = []
    non_num_headers = []
    numerical_values = Dict()
    non_num_values = Dict()
    describe_table = Dict()
    describe_non_num_table = Dict()
    for head in headers
        if (typeof(csv_file[head][2]) == Float64 || typeof(csv_file[head][2]) == Int64)
            push!(numerical_headers, head)
            numerical_values[head] = [elem for elem in csv_file[head]]
            describe_table[head] = []
            remove_missing(numerical_values, head, describe_table)
            describe_values(numerical_values, head, describe_table)
        else
            push!(non_num_headers, head)
            non_num_values[head] = [elem for elem in csv_file[head]]
            describe_non_num_table[head] = []
            remove_missing(non_num_values, head, describe_non_num_table)
            describe_non_num(non_num_values, head, describe_non_num_table)
        end
    end
    println("Description of the numerical features:")
    print_table(numerical_headers, describe_table)
    println("Description of the non-numerical features:")
    print_non_num_table(non_num_headers, describe_non_num_table)
else
    println("The file does not exist or is not a CSV file")
end
