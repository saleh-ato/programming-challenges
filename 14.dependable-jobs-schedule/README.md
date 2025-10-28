# **Dependable Jobs Schedule** ⚙️

Determine whether a set of jobs with dependencies can all be completed without circular references. This Ruby program checks dependency chains and detects cycles efficiently to ensure all jobs are finishable.

## **Repository Information**
- Main Repository: [Programming Challenges](https://github.com/saleh-ato/programming-challenges)
- Folder Path: `14.dependable-jobs-schedule/`
- Author: [Saleh Ato](https://github.com/saleh-ato)

***

## **Project Overview**
This repository includes a Ruby function, `finishAll()`, that verifies whether all jobs in a given dependency structure can be completed.  
Each job is represented by an integer from `0` to `jobs - 1`, and dependencies are defined as `[a, b]` meaning job `a` starts only after job `b` finishes.

- Input: `finishAll([jobs, dependencies])`
- Output: `true` (if all jobs can finish) or `false` (if a circular dependency exists)

***

## **Behavior Examples**
```ruby
finishAll([2, [[1, 0]]])
# Output: true

finishAll([2, [[1, 0], [0, 1]]])
# Output: false
# circular dependency

finishAll([3, [[1, 0], [2, 1]]])
# Output: true
# sequential chain 0→1→2

finishAll([1, []])
# Output: true
# only one job, no dependencies

finishAll([11, [[6, 10], [4, 3], [9, 2], [2, 3], [6, 1], [2, 8], [10, 1], [10, 2], [5, 3], [0, 10], [7, 4], [6, 1]]])
# Output: true
```

***

## **Implementation Approach**

### **Key Features**
- Detects cyclic dependencies between jobs.
- Processes complex dependency chains.
- Uses hash-based dependency tracking for simplification.

### **Core Functions**

**1️⃣ remove_single_and_prepare(jobs)**  
Prepares dependency data by removing independent jobs and flattening nested structures when necessary.

**2️⃣ create_queue(jobs)**  
Generates a mapping of dependent jobs into a hash for lookup and iteration.

**3️⃣ check_loop(queue)**  
Iteratively checks for circular references. Returns `false` upon detecting a loop.

**4️⃣ finishAll(array)**  
Combines all the above functions to return whether all jobs can be completed.

***

## **Code Example**
```ruby
def main()    
  puts finishAll([[1,2],[3,4],[2,3],[0,3]])        # true
  puts finishAll([[1,2],[2,3],[3,1]])              # false
  puts finishAll([[1,2],[2,3]])                    # true
  puts finishAll([2, [[1, 0]]])                    # true
  puts finishAll([2, [[1, 0], [0, 1]]])            # false
  puts finishAll([3, [[1, 0], [2, 1]]])            # true
  puts finishAll([1, []])                          # true
  puts finishAll([11, [[6,10],[4,3],[9,2],[2,3],[6,1],[2,8],
                       [10,1],[10,2],[5,3],[0,10],[7,4],[6,1]]]) # true
  puts finishAll([4, [[0,1],[1,2],[2,3],[3,0]]])   # false
end
main()
```

***

## **Setup and Execution**

### **Prerequisites**
- Ruby 3.x or higher installed on your system.

### **Run the Script**
```sh
ruby app.rb
```

***

## **How to Contribute**
1. Fork this repository.  
2. Create a new branch (`git checkout -b feature-xyz`).  
3. Implement your feature or fix.  
4. Commit and push changes (`git push origin feature-xyz`).  
5. Submit a pull request.

### **Possible Enhancements**
- Adding topological sort for validation.  
- Improving detection for deeply nested dependencies.  
- Building a visualization of dependency chains.

***

## **License**
Licensed under the MIT License – free for modification and redistribution.

***

## **Author**
Developed by [Saleh Ato](https://github.com/saleh-ato). Contributions are welcome!  
