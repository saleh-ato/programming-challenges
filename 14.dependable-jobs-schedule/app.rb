=begin
  Dependable Jobs Schedule
  You’re given a number of jobs and a list of dependencies.
  Each job is labeled from 0 to jobs - 1.
  Each dependency [a, b] means job a can only start after job b is finished.

  Return true if all jobs can be finished, or false if there’s a circular dependency.

  finishAll(2, [[1, 0]])
  output = True

  finishAll(2, [[1, 0], [0, 1]])
  output = False
  ## job 1 depends on job 0
  ## job 0 also depends on job 1
  ## → circular dependency, cannot complete either job

  finishAll(3, [[1, 0], [2, 1]])
  output = True
  ## job 0 → job 1 → job 2
  ## no cycles, all jobs can be finished in order

  finishAll(1, [])
  output = true
  ## only one job (0) with no dependencies
  ## → can be completed immediately

  finishAll(11, [[6, 10], [4, 3], [9, 2], [2, 3], [6, 1], [2, 8], [10, 1], [10, 2], [5, 3], [0, 10], [7, 4], [6, 1]])
  output = true
=end

def remove_single_and_prepare(jobs)
  jobs_copy=Marshal.load(Marshal.dump(jobs))
  jobs.each_with_index do |job,i|
    if job.class==Integer
      jobs_copy.delete(job) # Do not depended jobs.
    # elsif job.class==Array #Depended jobs
    #   # check_schedule(job,jobs)
    end
  end
  # print "Jobs Copy: ",jobs_copy.first, "\n"
  if jobs_copy.length == 1 && jobs_copy.first.is_a?(Array) && jobs_copy.first.first.is_a?(Array)
    return jobs_copy.first
  else
    return jobs_copy
  end
end

def create_queue(jobs)
  todo = {}
  # print jobs,"JOBS\n"
  jobs.each do |a,b|
    # print a,"\n\n"
    next if b.nil?
    todo[a]=b
  end
  # print "\ntodo: ", todo, "\n"
  return todo
end

def check_loop(queue)
  while true
    queue.dup.each do |key,value|
      # puts queue
      queue[key]=queue[queue[key]]
      return false if key==queue[key] 
      queue.delete(key) if queue[key]==nil
    end
    return true if queue=={}
    # puts queue
  end
end

def finishAll(array)
  return check_loop(create_queue(remove_single_and_prepare(array)))
end

def main()    
  puts finishAll([[1,2],[3,4],[2,3],[0,3]])      #true
  puts finishAll([ [1,2], [2,3], [3,1] ])        #false
  puts finishAll([ [1,2], [2,3] ])               #true
  puts finishAll([2, [[1, 0]]])                  #true
  puts finishAll([2, [[1, 0], [0, 1]]])          #false
  puts finishAll([3, [[1, 0], [2, 1]]])          #true
  puts finishAll([1, []])                        #true
  puts finishAll([11, [[6, 10], [4, 3], [9, 2], [2, 3], [6, 1], [2, 8], [10, 1], [10, 2], [5, 3], [0, 10], [7, 4], [6, 1]]]) # => true
  puts finishAll([4, [[0,1],[1,2],[2,3],[3,0]]]) #false
  puts finishAll([1, []])                        #true
end
main()