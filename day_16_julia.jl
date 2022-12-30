
global connections=Dict{Int64,Tuple}()
global flow_rate=Dict{Int64,Int64}()
global start=1

function parse_input(file)
    lines=[]

    open(file) do f
        while !eof(f) push!(lines,strip(readline(f))) end
    end

    global start
    ind=Dict{String,Int64}()
    for k=1:length(lines) 
        name=(lines[k])[7:8]
        ind[name]=k 
        if name=="AA" start=k end
    end

    global connections
    global flow_rate
    reg=r"Valve \w\w has flow rate=(\d*); tunnel\w? lead\w? to valve\w? (.*)"

    for k=1:length(lines)
        m=match(reg,lines[k])
        flow_rate[k]=parse(Int64,m[1])
        neighbors=[ind[s] for s in rsplit(m[2],", ")]
        connections[k]=Tuple(neighbors)
    end

end

let 

SEEN=Dict{Tuple,Int64}()

global max_pressure
function max_pressure(x,openV,time,players)
    if length(SEEN)%100000==0 println(length(SEEN)) end

    if time==1 return (players==1) ? 0 : max_pressure(start,openV,26,players-1) end

    id=(x,openV,time,players)
    if haskey(SEEN,id) return SEEN[id] end

    ans=0

    for n in connections[x] ans=max(ans,max_pressure(n,openV,time-1,players)) end

    if flow_rate[x]>0 && openV[x] == '0'
        new_openV=openV[1:x-1]*"1"*openV[x+1:end]
        ans=max(ans,max_pressure(x,new_openV,time-1,players)+(time-1)*flow_rate[x])
    end

    SEEN[id]=ans
    return ans
end

end

function part2()
    pressure=max_pressure(start,"0"^63,26,2)
    println(pressure)
end
