include("./count_values.jl")
include("./sum_values.jl")
include("./min_values.jl")
include("./standard_deviation.jl")
include("./max_values.jl")
#=
    1. Count
    2. Mean
    3. Std
    4. Min
    5. Q1
    6. Q2
    7. Q3
    8. Max
=#
function describe_values(numerical_values, head, describe_table)
    push!(describe_table[head], count_values(numerical_values[head]))
    sum_elem = sum_values(numerical_values[head])
    push!(describe_table[head], sum_elem / describe_table[head][1])
    push!(describe_table[head], standard_deviation(describe_table[head][2], numerical_values[head]))
    push!(describe_table[head], min_values(numerical_values[head]))
    sort!(numerical_values[head])
    push!(describe_table[head], numerical_values[head][Int(round(describe_table[head][1]/4))])
    push!(describe_table[head], numerical_values[head][Int(round(describe_table[head][1]/2))])
    push!(describe_table[head], numerical_values[head][Int(round(describe_table[head][1]/4*3))])
    push!(describe_table[head], max_values(numerical_values[head]))
end