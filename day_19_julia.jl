let

SEEN=Dict{Tuple,Int64}()

global geodes_produced
function geodes_produced(time,Or,Cl,Ob,Ge,Or_r,Cl_r,Ob_r,Ge_r,Or_c,Cl_c,Ob_c0,Ob_c1,Ge_c0,Ge_c1)
    #if length(SEEN)%10000==0 println(length(SEEN)) end

    if time==1 return Ge+Ge_r end

    no_Or,no_Cl,no_Ob=false,false,false
    if Or >= time*max(Ge_c0,Ob_c0,Cl_c,Or_c) || (Or_r >= max(Ge_c0,Ob_c0,Cl_c,Or_c) && Or>= max(Ge_c0,Ob_c0,Cl_c,Or_c))
        Or=time*max(Ge_c0,Ob_c0,Cl_c,Or_c)
        Or_r=0
        no_Or=true
    end

    if Cl >= time*Ob_c1 || (Cl_r >= Ob_c1 && Cl >= Ob_c1)
        Cl=time*Ob_c1
        Cl_r=0
        no_Cl=true
    end

    if Ob >= time*Ge_c1 || (Ob_r >= Ge_c1 && Ob >= Ge_c1)
        Ob=time*Ge_c1
        Ob_r=0
        no_Ob=true
    end

    state=(time,Or,Cl,Ob,Ge,Or_r,Cl_r,Ob_r,Ge_r,Or_c,Cl_c,Ob_c0,Ob_c1,Ge_c0,Ge_c1)

    if haskey(SEEN,state) return SEEN[state] end

    new_Or,new_Cl,new_Ob,new_Ge=Or+Or_r,Cl+Cl_r,Ob+Ob_r,Ge+Ge_r

    if Or>=Ge_c0 && Ob>=Ge_c1
        ans=geodes_produced(time-1,new_Or-Ge_c0,new_Cl,new_Ob-Ge_c1,new_Ge,Or_r,Cl_r,Ob_r,Ge_r+1,Or_c,Cl_c,Ob_c0,Ob_c1,Ge_c0,Ge_c1)
        SEEN[state]=ans
        return ans
    end

    ans=geodes_produced(time-1,new_Or,new_Cl,new_Ob,new_Ge,Or_r,Cl_r,Ob_r,Ge_r,Or_c,Cl_c,Ob_c0,Ob_c1,Ge_c0,Ge_c1)

    if !no_Ob && Or>=Ob_c0 && Cl>=Ob_c1
        ans=max(ans,geodes_produced(time-1,new_Or-Ob_c0,new_Cl-Ob_c1,new_Ob,new_Ge,Or_r,Cl_r,Ob_r+1,Ge_r,Or_c,Cl_c,Ob_c0,Ob_c1,Ge_c0,Ge_c1))
    end

    if !no_Cl && Or>=Cl_c
        ans=max(ans,geodes_produced(time-1,new_Or-Cl_c,new_Cl,new_Ob,new_Ge,Or_r,Cl_r+1,Ob_r,Ge_r,Or_c,Cl_c,Ob_c0,Ob_c1,Ge_c0,Ge_c1))
    end
    
    if !no_Or && Or>=Or_c
        ans=max(ans,geodes_produced(time-1,new_Or-Or_c,new_Cl,new_Ob,new_Ge,Or_r+1,Cl_r,Ob_r,Ge_r,Or_c,Cl_c,Ob_c0,Ob_c1,Ge_c0,Ge_c1))
    end
    
    SEEN[state]=ans
    return ans

end

end

function part1(file)
    tot=0
    k=0
    open(file) do f
        while ! eof(f) 
            k+=1
            l=split(strip(readline(f))," ")
            Or_c=parse(Int64,l[7])
            Cl_c=parse(Int64,l[13])
            Ob_c0=parse(Int64,l[19])
            Ob_c1=parse(Int64,l[22])
            Ge_c0=parse(Int64,l[28])
            Ge_c1=parse(Int64,l[31])
            
            ans=geodes_produced(24,0,0,0,0,1,0,0,0,Or_c,Cl_c,Ob_c0,Ob_c1,Ge_c0,Ge_c1)
            tot+=k*ans
            println(k,": ",ans)

        end
    end

    println(tot)
end

function part2(file)

    res=[]
    open(file) do f
        for k=1:3
            l=split(strip(readline(f))," ")
            Or_c=parse(Int64,l[7])
            Cl_c=parse(Int64,l[13])
            Ob_c0=parse(Int64,l[19])
            Ob_c1=parse(Int64,l[22])
            Ge_c0=parse(Int64,l[28])
            Ge_c1=parse(Int64,l[31])
            
            ans=geodes_produced(32,0,0,0,0,1,0,0,0,Or_c,Cl_c,Ob_c0,Ob_c1,Ge_c0,Ge_c1)
            push!(res,ans)
            println(k,": ",ans)

        end
    end

    println(res[1]*res[2]*res[3])

end