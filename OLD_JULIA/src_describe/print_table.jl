using DataFrames
using PrettyTables
showln(x) = (show(x); println())

#=
    We put all the datas in a Dataframe
    We then use PrettyTable.jl to print it nicely
=#
function print_table(numerical_headers, describe_table)
    headers = ["Features"]
    for elem in numerical_headers
        push!(headers, String(elem))
    end
    df = DataFrame(Subjects = ["Missing", "Count", "Mean", "Std", "Min", "25%", "50%", "75%", "Max"])
    i = 1
    for elem in numerical_headers
        i += 1
        insert!(df, i, describe_table[elem], :elem)
        rename!(df, Symbol("elem")=>Symbol(elem))
    end
    pretty_table(df,
                    header_crayon = crayon"yellow bold",
                    formatters = ft_printf("%5.2f"))
end