include("./count_values.jl")
include("./sum_values.jl")
include("./min_values.jl")
include("./standard_deviation.jl")
include("./max_values.jl")
#=
    1. Missing elements (already added in remove_missing())
    2. Count
    3. Mean
    4. Std
    5. Min
    6. Q1
    7. Q2
    8. Q3
    9. Max
=#
function describe_values(numerical_values, head, describe_table)
    push!(describe_table[head], count_values(numerical_values[head]))
    sum_elem = sum_values(numerical_values[head])
    push!(describe_table[head], sum_elem / describe_table[head][2])
    push!(describe_table[head], standard_deviation(describe_table[head][3], numerical_values[head]))
    push!(describe_table[head], min_values(numerical_values[head]))
    sort!(numerical_values[head])
    push!(describe_table[head], numerical_values[head][Int(round(describe_table[head][2]/4))])
    push!(describe_table[head], numerical_values[head][Int(round(describe_table[head][2]/2))])
    push!(describe_table[head], numerical_values[head][Int(round(describe_table[head][2]/4*3))])
    push!(describe_table[head], max_values(numerical_values[head]))
end