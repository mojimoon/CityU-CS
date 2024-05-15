# CS3103 Operating Systems - Review

## 1. Introduction

**Operating System (OS)**: Intermediary program between application software and hardware.

Computer System Architecture: Hardware → OS → Application → User

Computer Organization: System bus connects CPU, memory, I/O devices (disk controller, USB controller, etc.)

**Interrupt**: Signal to CPU that an event has occurred. CPU transfers control from current program to **Interrupt Service Routine (ISR)**.

- Hardware Interrupt: Hardware device sends signal (e.g. I/O request)
- Software Interrupt: Program requests OS service (e.g. system call)
- ISR nvolves **context switching** (save current program state, load ISR state)

Current Program → Interrupt → ISR → Scheduler → Next Program

**Timer Interrupt**: Periodic interrupt to prevent infinite loops, enforce time limits. (software interrupt)

**Storage Hierarchy**: Primary (Register → Cache → Main Memory) → Secondary (NVMe SSD → HDD) → Tertiary (Cold Storage)

### Kernel

- **Kernel**: Core part of OS, manages system resources, provides services to applications.
- **System Programs**: Extend kernel functionality, provide services to users.
- **Privileged Instructions**: Instructions that can only be executed in kernel mode.
- **Monolithic Kernel**: All OS services (Kernel + System Programs) in kernel space. (UNIX, Linux, Windows)
- **Microkernel**: Only essential services in kernel space, other services in user space. (MacOS, Windows NT)
- **Shell**: A OS component which exposes OS services to users.
    - CLI (Command Line Interface): Text-based
    - GUI (Graphical User Interface): Graphical
- **System Calls**: Interface to OS services, invoked by user programs.
    - **Application Programming Interface (API)**: Platform-independent interface to OS services.
- Implenetation of OS
    - **Mechanism**: The framework that provides the service
    - **Policy**: The algorithm that determines how the service is provided
    - e.g. compression is a mechanism, LZW is a policy

### Types of OS

- UNIX
    - Linux: Open-source UNIX-like OS
    - Android: A middleware (OS + some applications) based on Linux and Java
- **Real-time Operating System (RTOS)**: OS that guarantees a certain response time for critical tasks
    - Event-driven, preemptive
- **POSIX**: Portable Operating System Interface for UNIX
    - Standard for OS compatibility
    - Defines API, shell, utilities, etc.
- **Virtual Machine (VM)**: Software that emulates hardware, allowing multiple OS to run on the same hardware

## 2. Process

- **Program**: Static code, stored on disk.
- **Process**: A program in execution (in main memory).
- **Thread**: Smallest unit of execution within a process.

Memory Layout: Text (code) → Data (global variables) → Heap (dynamic memory) → Stack (local variables, function calls)

Each thread has its own stack, but shares code, data, heap.

### Process States

- **New**: Being created
- **Ready**: Ready to run
- **Running**: Currently executing
- **Waiting**: Blocked, waiting for event (e.g. I/O)
- **Terminated**: Finished execution

**Process Control Block (PCB)**: Processes as seen by OS. Contains PID, process state, PC, registers, etc.

Process queues:

- **Job Queue**: All processes in system
- **Ready Queue**: Processes in main memory (state: ready, waiting)
- **Device Queue**: Processes waiting for I/O (state: waiting)

Scheduler:

- **Job Scheduler**: Selects processes from job queue into ready queue
    - Long-term scheduler
    - **Multiprogramming**: Multiple processes in memory so that CPU always has something to execute
- **CPU Scheduler**: Selects process from ready queue to run
    - Short-term scheduler
    - **Multitasking**: Frequently switching between processes to create illusion of parallelism (concurrent execution)

Types of processes:

- CPU-bound: Few long CPU bursts
- I/O-bound: Many short CPU bursts

### Context Switching

- Save the state of the current process
- Load the state of the next process
- Both steps must be done in kernel mode, so each context switching involves 2 mode switches

```c
pid = fork(); // Create child process. Return 0 in child, child PID in parent
execlp("/bin/ls", "ls", NULL); // Replace current process with new program (ls)
getpid(); // Get PID of current process
getppid(); // Get PID of parent process
```

Steps in process creation:

1. Load code (text segment) and data (global variables) into memory
    - **Lazy Loading**: Load only when needed
2. Allocate stack (local variables, function calls)
3. Allocate heap (dynamic memory)
4. Initialize I/O, files, etc.
5. Start execution at entry point (main function)

Process termination:

- **Exit**: Process calls `exit()`
    - return data to parent process
    - OS deallocates resources
- **Abort**: Parent process terminates child, happens when
    - Child process is no longer needed
    - Child process exceeds resource limits
    - Parent process is terminating

### Inter-Process Communication (IPC)

Goal of IPC: Allow processes to communicate and synchronize

- **Message Passing**: Each process has a queue for incoming messages
    - **Direct Communication**: Processes must name each other explicitly
        - Properties: Links are established automatically, each link is associated with exactly 1 pair of processes, each pair has exactly 1 link
    - **Indirect Communication**: Messages sent to mailbox, identified by ID
        - Properties: Link is proactively established, each link can be associated with multiple processes, each pair can have multiple links
    - Blocking (synchronous) vs Non-blocking (asynchronous)
- **Shared Memory**: Processes share a region of memory
    - A region of memory is allocated, and processes can read/write to it

Comparison:

| Message Passing | Shared Memory |
| --- | --- |
| Distributed systems | Single system |
| OS provides communication | Programmer implements communication |
| Slower | Faster |

UNIX Socket: Communication endpoint for inter-process communication

**Remote Procedure Call (RPC)**: Procedure call that appears to be local but is executed remotely

## 3. Threads

Thread: Smallest unit of execution and scheduling

**Multi-threading**: Multiple threads in a single process

- For parallelism: Execute multiple threads simultaneously on multiple CPUs
- For higher CPU utilization: Keep CPU busy when one thread is blocked (e.g. I/O)

**Parallelism**: Multiple threads/processes executing over different cores simultaneously

**Concurrency**: Multiple threads/processes executing on a single core, interleaved

Comparison with processes:

| | Process | Thread |
| --- | --- | --- |
| Dedicated memory | Data, code, heap, stack | Stack, registers |
| Context switching | Expensive | Cheap |
| Inter communication | IPC | Shared memory |

### User/Kernel Threads

- **User-level threads**: Managed by user-level threads library
    - OS cannot see threads, treats process as single-threaded
    - Fast context switching
- **Kernel-level threads**: Managed by OS
    - OS schedules threads
    - Slower context switching

ULT must be mapped to KLT for scheduling

- **One-to-One**: Each ULT maps to a KLT
    - Issue: Creating many KLTs can be expensive
- **Many-to-One**: Many ULTs map to a single KLT
    - Issue: Blocking system calls block all threads; Parallelism not achieved
- **Many-to-Many**: Many ULTs map to many KLTs
- **Combined Model**: One-to-One and Many-to-Many

Comparison:

| | ULT | KLT |
| --- | --- | --- |
| Implementation | User-level library | OS |
| Context switching | Fast | Slow |
| Blocking | One thread blocks all | Only blocking thread blocks |
| System Mode | * | Kernel Mode |

*: ULT can be schedule in User Mode (M:1 model), but preemption and blocking cannot be handled in User Mode

### Lifecycle of a Thread

**Cancellation**: Terminating a thread before it completes

- **Asynchronous cancellation**: Terminate immediately (no guarantee)
    - May cause resource leaks
- **Deferred cancellation**: Check cancellation status at cancellation points

**Thread Pool**: Pre-allocate threads for reuse

Advantages of thread pools:

- Faster than creating new threads
- Allow bounded number of threads (limit the number of threads owned by one process)

**Pthreads**: POSIX standard for thread creation and synchronization

```c
pthread_t p1; // Thread ID
pthread_create(&p1, NULL, function, arg); // Create thread
pthread_join(p1, NULL); // Wait for thread to finish
// the second argument is where the return value of the thread is stored
```

### Thread Context Switching

- Context of a process: address space (code, data, heap, stack), registers, resources
- Context of a thread: Registers, stack

Steps in context switching:

1. Interrupt occurs
2. **Context protection**: Save registers of current thread to stack
    - Reasons: ISR need to use registers (in PCB); interrupt is asynchronous
3. **Context switch**: Load registers of next thread from stack
4. Return from interrupt

## 4. Scheduling

Goal of scheduling: Maximize CPU utilization, concurrency

**CPU Scheduler**: Selects process from ready queue to run

**Dispatcher**: Switches context, transfers control to selected process

Interrupt → ISR (KM → Context Protection → UM) → Scheduler → Dispatcher (KM → Context Switch → UM) → Next Process

Metrics:

- **CPU Utilization**: Percentage of time CPU is busy
- **Throughput**: $\text{Number of processes completed} / \text{Time}$
- **Waiting Time**: Time spent in ready queue
- **Turnaround Time**: $t_{\text{completion}} - t_{\text{arrival}}$
- **Response Time**: $t_{\text{first execution}} - t_{\text{arrival}}$

### Scheduling Algorithms

- **First-Come, First-Served (FCFS)** (non-preemptive)
- **Shortest Job First (SJF)** (non-preemptive or preemptive)
    - **Shortest Remaining Time First (SRTF)**: Preemptive SJF
    - Optimal in terms of average waiting time
    - Cannot determine burst time in advance
    - Estimates burst time based on previous burst times: $\tau_{n+1} = \alpha t_n + (1 - \alpha) \tau_n$ where $t_n$ is the actual burst time and $\tau_n$ is the estimated burst time
- **Priority Scheduling** (non-preemptive or preemptive)
    - Smallest number is highest priority
- **Round Robin (RR)** (preemptive)
    - Time quantum $q$
    - No process waits more than $(n-1)q$ time units
    - Large $q$: FCFS; Small $q$: Context switching overhead
- **Multi-Level Queue**
    - Separate queues for different types of processes
    - Each queue has its own scheduling algorithm
    - Scheduling is also done between queues (priority or time slice)
    - Multilevel feedback queue: Move processes between queues based on behaviour

Linux scheduling:

- Default: **Completely Fair Scheduler (CFS)**
    - Each process is assigned a nice value (smaller value = higher priority)
    - **Virtual Runtime**: Weighted sum of actual runtime and priority `vruntime += runtime * nice`
    - Scheduler picks process with smallest `vruntime`
- Real-time: Priority-based
- Real-time tasks have higher priority than CFS tasks

## 5. Synchronization

**Race Condition**: Multiple threads access shared data concurrently, leading to incorrect results

**Critical Section**: Part of code that accesses shared data

Goal of synchronization

- **Mutual Exclusion**: Only one thread can access CS at a time
- **Progress**: If no thread is in CS, a thread can enter
- **Bounded Waiting**: A thread cannot wait for more than $C$ times that another thread has entered CS
- **Independence**: No assumption about speed, number of CPUs

### Mutex

```c
// P0
do {
    flag[0] = true; turn = 1;
    while (flag[1] && turn == 1);
    // Critical section
    flag[0] = false;
    // Remainder section
} while (1);

// P1
do {
    flag[1] = true; turn = 0;
    while (flag[0] && turn == 0);
    // Critical section
    flag[1] = false;
    // Remainder section
} while (1);
```

- `turn` indicates whose turn it is to enter CS
- `flag` indicates if a process is ready to enter CS
- **Mutual Exclusion**: Only one process can be in CS
    - If P0 is in CS → `flag[0] = true` → P1 cannot enter CS
    - If both P0 and P1 are ready to enter CS → `turn` decides who enters first
- **Progress**: If no process is in CS, a process can enter
    - If P0 wants to enter CS and no process is in CS → `flag[1] = false` → P0 can enter
- **Bounded Waiting**: P1 waits for P0 to enter CS at most once
    - When P0 exits CS → `flag[0] = false` → P1 can enter CS
    - Should P0 sets `flag[0] = true` before P1 can enter CS, given that `turn = 1`, P1 can enter CS
    - Should P0 sets `flag[0] = true` before P1 can enter CS, given that `flag[1] = true`, P0 cannot enter CS again

**Atomic Operation**: Operation that appears to be executed in a single step. Done by hardware.

```c
bool TestAndSet(bool *lock) {
    bool old = *lock;
    *lock = true;
    return old;
}

// P0
do {
    while (TestAndSet(&lock));
    // Critical section
    lock = false;
    // Remainder section
} while (1);
```

Explanation: `TestAndSet` is an atomic operation that returns the original value and sets the value to `true`. If `lock` is `false`, the lock is acquired and the process can enter CS. If `lock` is `true`, the process waits until `lock` is `false`.

```c
void swap(bool *a, bool *b) {
    bool temp = *a;
    *a = *b;
    *b = temp;
}

// P0
do {
    key = true;
    while (key) swap(&lock, &key);
    // Critical section
    lock = false;
    // Remainder section
} while (1);
```

Explanation: `lock` is a global variable that indicates if the CS is occupied. `key` is a local variable that indicates if the process wants to enter CS. If `lock` is `true`, swap results in `lock=true` and `key=true` so that the process waits. If `lock` is `false`, swap results in `lock=true` and `key=false` so that the process enters CS.

### Semaphores

**Semaphore**: Integer variable that can be accessed only through two atomic operations: `wait()` and `signal()`

Can be counting or binary

```c
void wait(Semaphore s) {
    while (s <= 0);
    s--; // acquire resource
}
void signal(Semaphore s) {
    s++; // release resource
}

// P0
do {
    wait(s);
    // Critical section
    signal(s);
    // Remainder section
} while (1);
```

The above implementation is a **spinlock**. The process keeps checking the semaphore until it is available. Causes busy waiting.

**Semaphore waiting queue**: Processes that cannot acquire the semaphore are placed. Two operations:

- **Block**: Put the calling process in the waiting queue
- **Wakeup**: Remove a process from the waiting queue and put it in the ready queue

```c
void wait(Semaphore s) {
    s--;
    if (s < 0) {
        block();
    }
}
void signal(Semaphore s) {
    s++;
    if (s <= 0) {
        Thread t = s.queue.dequeue();
        wakeup(t);
    }
}
```

If no more resources are available, the process is blocked. Negative semaphore value indicates the number of processes waiting.

If the resource is released and there are processes waiting, wake up one process.

### Classical Problems

**Producer-Consumer Problem**: Producer produces items and puts them in a buffer. Consumer consumes items from the buffer.

3 semaphores:

- `mutex` (binary, initiallized to 1): Mutual exclusion for buffer access
- `full` (counting, initialized to 0): Number of occupied slots in buffer
- `empty` (counting, initialized to buffer size): Number of empty slots in buffer

```c
// Producer
do {
    produce(item);
    wait(empty);
    wait(mutex);
    // critical section start
    put_item_into_buffer(item);
    // critical section end
    signal(mutex);
    signal(full);
} while (1);

// Consumer
do {
    wait(full);
    wait(mutex);
    // critical section start
    item = get_item_from_buffer();
    // critical section end
    signal(mutex);
    signal(empty);
    consume(item);
} while (1);
```

**Readers-Writers Problem**: Multiple readers can read simultaneously, but only one writer can write at a time. No reading while writing.

2 semaphores:

- `mutex` (binary, initialized to 1): Protects `readcount`
- `wrt` (binary, initialized to 1): Writer wants to write

1 shared variable:

- `readcount` (initialized to 0): Number of readers reading

```c
// Writer
do {
    wait(wrt);
    write();
    signal(wrt);
} while (1);

// Reader
do {
    wait(mutex);
    readcount++;
    if (readcount == 1) wait(wrt); // the first reader blocks writer
    signal(mutex);
    read();
    wait(mutex);
    readcount--;
    if (readcount == 0) signal(wrt); // the last reader unblocks writer
    signal(mutex);
} while (1);
```

**Dining Philosophers Problem**: 5 philosophers sit at a table with 5 forks. Each philosopher needs 2 forks to eat.

1 semaphore per fork:

- `forks[5]` (binary, initialized to 1)

```c
do {
    wait(forks[i]);
    wait(forks[(i+1) % 5]);
    eat();
    signal(forks[i]);
    signal(forks[(i+1) % 5]);
    think();
} while (1);
```

Issue: if philosopher `i` picks up `forks[i]` but `i+1` picks up `forks[(i+1) % 5]`, and this forms a cycle, a deadlock occurs.

### Condition Variables

```c
pthread_cond_t cond = PTHREAD_COND_INITIALIZER;
pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;
int done = 0;

void thr_exit() {
    pthread_mutex_lock(&mutex);
    done = 1;
    pthread_cond_signal(&cond);
    pthread_mutex_unlock(&mutex);
}

void* child(void *arg) {
    do_something(arg);
    thr_exit();
    return NULL;
}

void thr_join() {
    pthread_mutex_lock(&mutex);
    if (!done) {
        pthread_cond_wait(&cond, &mutex);
    }
    pthread_mutex_unlock(&mutex);
}
```

The parent checks if the child is done. If not, it puts itself to sleep and waits for the child to signal it.

The child sets `done` to 1 and signals the parent upon completion.

If mutex is absent, race condition occurs. If condition variable is absent, indefinite waiting occurs.

Producer-Consumer with condition variables:

```c
cond_t empty, full;
mutex_t mutex;

void* producer(void *arg) {
    int i;
    for (i = 0; i < N; i++) {
        pthread_mutex_lock(&mutex);
        while (count == BUFFER_SIZE) // full
            pthread_cond_wait(&empty, &mutex); // release mutex and sleep until signaled
        put(i);
        pthread_cond_signal(&full); // signal consumer
        pthread_mutex_unlock(&mutex);
    }
}

void* consumer(void *arg) {
    int i, item;
    for (i = 0; i < N; i++) {
        pthread_mutex_lock(&mutex);
        while (count == 0) // empty
            pthread_cond_wait(&full, &mutex); // release mutex and sleep until signaled
        item = get();
        pthread_cond_signal(&empty); // signal producer
        pthread_mutex_unlock(&mutex);
        printf("%d\n", item);
    }
}
```

- **Mesa Semantics**: No guarantee that when the woken thread runs, the condition is still true
- **Hoare Semantics**: Guarantee that the woken thread runs immediately

## 6. Deadlocks

**Deadlock**: A set of blocked processes each holding a resource and waiting to acquire a resource held by another process

Necessary conditions:

- **Mutual Exclusion**: At least one resource must be non-shareable
- **Hold and Wait**: Process holds a resource and waits for another held by other processes
- **No resource preemption**: Resources can only be released after the process is done
- **Circular wait**: A cycle of processes waiting for resources

**Resource Allocation Graph**:

- **Resource**: $R_1, R_2, \ldots, R_m$ Each resource type has $W_i$ instances
- **Process**: $P_1, P_2, \ldots, P_n$
- **Request edge**: $P_i \to R_j$ Process $P_i$ requests resource $R_j$
- **Assignment edge**: $R_j \to P_i$ Resource $R_j$ is assigned to process $P_i$

Reading RAG:

- If a graph has no cycle, no deadlock
- If a graph has a cycle,
    - If there is only one instance of each resource type, deadlock
    - If there are multiple instances of a resource type, possibility of deadlock

### Deadlock Prevention

Ensure that at least one of the necessary conditions does not hold.

- Circular wait: Provide a **total ordering** of resources such that each process requests resources in increasing order
- Hold and wait: Process must request all resources at once (atomically)
    - Issue: Low resource utilization; starvation; decrease concurrency
- No preemption: use `trylock()` which tries to acquire a lock and returns immediately if it cannot
    - Issue: **livelock** (processes keep changing state but cannot make progress)
    - Solution: add a random delay before retrying
- Mutual exclusion: use atomic hardware instructions

```c
int CompareAndSwap(int *ptr, int old, int new) {
    int temp = *ptr;
    if (temp == old) {
        *ptr = new;
        return 1;
    }
    return 0;
}
```

This function atomically compares the value at `ptr` with `old` and updates it to `new` if they are equal. After successful update, it returns 1. Otherwise, it returns 0.

This does not involve a explicit lock and thus deadlock-free.

### Deadlock Avoidance

Ensure that the system will never enter unsafe state. Specifically, ensure that the circular wait condition is never satisfied.

Requires knowledge of future resource requests.

**Safe state**: A state where there exists a sequence $<P_1, P_2, \ldots, P_n>$ such that the resources requested by $P_i$ can be satisfied by currently available resources and resources held by $P_j$ where $j < i$. Therefore, executing the sequence will not lead to deadlock, and the sequence is called a **safe sequence**.

Single-instance resources: Resource allocation graph

3 types of edges:

- **Request edge**: $P_i \to R_j$
- **Assignment edge**: $R_j \to P_i$
- **Claim edge**: $P_i \to R_j$ (dash line) Process $P_i$ may request resource $R_j$ in the future

Transitions between states:

- Claim edge → Request edge: Process requests resource
- Request edge → Assignment edge: Resource is allocated
- Assignment edge → Claim edge: Resource is released

If converting a request edge to an assignment edge results in a cycle, the system is in an unsafe state.

Multiple-instance resources: Banker's algorithm

- Each process must a priori declare the maximum number of each resource type it may need
- Data structures: `n` processes, `m` types of resources
    - `available[m]`: Number of available resources of each type
    - `max[n][m]`: Maximum demand of each process
    - `allocation[n][m]`: Number of resources of each type currently allocated to each process
    - `need[n][m] = max - allocation`: Remaining resources needed by each process

```python
def is_safe(processes, available, _max, allocation):
    work = available # simulate available resources
    finish = [False] * len(processes)
    need = _max - allocation
    while True:
        found = False
        for i in range(len(processes)):
            if not finish[i] and all(need[i] <= work):
                work += allocation[i]
                finish[i] = True
                found = True
        if not found:
            break # failed to find a process to execute
    return all(finish)

def allocate(i, request): # process i requests for request[m] resources
    if not all(request <= need[i]):
        raise Exception("Request exceeds need")
    if not all(request <= available):
        return False # process must wait
    for j in range(m):
        available[j] -= request[j]
        allocation[i][j] += request[j]
        need[i][j] -= request[j]
    if not is_safe(processes, available, _max, allocation):
        # rollback
        for j in range(m):
            available[j] += request[j]
            allocation[i][j] -= request[j]
            need[i][j] += request[j]
        return False # process must wait
    return True # request granted
```

Deadlock avodiance require **global knowledge** of the system state.

- Know which processes will request which resources
- Can schedule in a way to guarantee no deadlock

### Deadlock Detection

Allow system to enter deadlock state, then recover.

Single-instance resources: Wait-for graph

**Wait-for graph**: Directed graph where nodes are processes and edges are requests

There is an edge $P_i \to P_j$ if $P_i$ is waiting for $P_j$ to release a resource.

If the graph has a cycle, there is a deadlock.

Multiple-instance resources:

```python
def detect_deadlock(processes, available, _max, allocation, request):
    # request[n][m] is the current request of each process
    work = available
    finish = [False] * len(processes)
    need = _max - allocation
    while True:
        found = False
        for i in range(len(processes)):
            if not finish[i] and all(request[i] <= work):
                work += allocation[i]
                finish[i] = True
                found = True
        if not found:
            break # failed to find a process to execute
    if all(finish):
        return False # no deadlock
    return True # deadlock
```

Difference from deadlock avoidance: Use `request[i] <= work` instead of `need[i] <= work`

Deadlock recovery:

- **Process termination**: Abort a process at a time until the cycle is broken
- **Resource preemption**: Select a victim, preempt resources, rollback

## 7. Memory Management

- **Logical Address**: Address generated by CPU
- **Physical Address**: Address seen by memory unit
- Same in compile-time and load-time address binding
- Different in execution-time address binding

**Memory Management Unit (MMU)**: Translates logical address to physical address

**Swapping**: Move a process from main memory to disk, and vice versa

**Hole**: Block of available memory

**Dynamic Storage-Allocation Problem**: allocate memory holes to processes

**Fragmentation**:

- **Internal Fragmentation**: allocated memory is larger than requested memory
- **External Fragmentation**: total memory space exists to satisfy a request, but it is not contiguous

**Compaction**: Shuffle memory contents to place all free memory together, to reduce external fragmentation

### Paging

- Physical memory divided into fixed-size **frames**
- Logical memory divided into fixed-size **pages**
- Keep track of free frames
- **Page table** maps logical pages to physical frames
- Eliminates external fragmentation

Address translation:

- Virtual address = **VPN** (Virtual Page Number) + Offset
- Translate VPN to PFN (Physical Frame Number) using page table

**Page Table**: a data structure that maps virtual pages to physical frames

- Each process has its own page table
- Page table is stored in main memory

**Page Table Entry (PTE)**: Contains frame number, protection bits, etc.

Simple linear page table:

- Row number: VPN
- Each row: valid bit, PFN

Issues: large page tables

For a $b$-bit address space where $p$ bits are used for VPN:

- There are $2^p$ entries
- Each entry is $\frac{b}{8}$ bytes
- Total size: $2^p \times \frac{b}{8}$ bytes

Can be mitigated by larger page size (less entries), but leads to internal fragmentation

**Translation Lookaside Buffer (TLB)**: Cache for page table entries (hardware)

- If entry is not in TLB, look up page table in main memory

**Hierarchical Page Table**: Reduce page table size

Advantage:

- Allocate page table only for pages in use
- Allow dynamic growth of page tables

Disadvantage:

- Time to access page table increases

Steps:

1. Read the page `PBDR`, find value at `PDE index` (high bits of VPN) as `PTE`
2. Read the page `PTE`, find value at `PTE index` (low bits of VPN) as `PFN`
3. Read the page `PFN`, find value at `offset`

Example:

- Virtual address space: 15-bit (32KB)
- Page size: 32 bytes
- Number of pages: $2^{15} / 2^5 = 1024$
- VPN: 10 bits
- Offset: 5 bits
- Page entry per page: 32 PTEs
- Physical address space: 12-bit (4KB)
- Number of frames: $2^{12} / 2^5 = 128$

Since there are 32 PTEs in VPN, the last 5 bits of VPN are used to index the PTE. Therefore, the first 5 bits of VPN are used to index the PDE.

- bit 14-10: PDE index
- bit 9-5: PTE index
- bit 4-0: offset

Example: virtual address `0x611c = 0110 0001 0001 1100`

- PDE index = `11000` = 24
- PTE index = `01000` = 8
- offset = `11100` = 28
- Given PBDR = 108

1. Read page PBDR (108), find column PDE index (24) as PTE
    - value: `0xa1 = 1010 0001`, valid bit = 1, PTE = `010 0001` = 33
2. Read page PTE (33), find column PTE index (8) as PFN
    - value: `0xb5 = 1011 0101`, valid bit = 1, PFN = `011 0101` = 53
3. Read page PFN (53), find column offset (28)
    - value: `0x08`

Therefore the value at virtual address `0x611c` is `0x08`.

### Segmentation

View memory as a collection of segments

## 8. Page Replacement

**Demand Paging**: A page system with swapping.

To execute a program on disk, swap pages into memory as needed.

If the program tries to access a page not in memory, a page fault occurs.

Each page table entry has a valid-invalid bit. 1 if in memory, 0 if not.

During execution, when a page table entry with 0 is accessed, a page fault occurs.

Handling page faults:

- Find a free frame in memory
- Swap page into frame
- Update page table and set valid bit to 1
- Restart the instruction that caused the page fault

**Page Replacement**: if no free frame, replace a page

Performance metrics:

- Page fault rate $p$
- Effective access time $EAT = (1 - p) \times \text{memory access time} + p \times \text{page fault time}$

### Page Replacement Algorithms

- **FIFO**: Replace oldest page
- **LRU**: Replace least recently used page
    - Counter-based:
        - Maintain a counter for each page
        - When a page is accessed, copy the current time to the counter $O(1)$
        - Replace the page with the smallest counter $O(n)$
    - Stack-based:
        - Maintain a doubly linked list of pages
        - When a page is accessed, move it to the top of the stack $O(1)$
        - Replace the page at the bottom of the stack $O(n)$
- Second-chance (clock): FIFO with a reference bit (initially 0)
    - When a page is accessed, set the reference bit to 1
    - To replace a page, if the reference bit is 1, set it to 0 and move to the next page
    - Replace the first page with reference bit 0
    - Pages are visited in a circular manner

Allocation of frames among processes:

- Equal allocation: Allocate equal number of frames to each process
- Proportional allocation: Allocate frames based on the size of the process
- Priority allocation: Allocate frames based on priority

Replacement Scope:

- **Local replacement**: Replace a page in the process that caused the page fault
    - Issue: Process slows down even if other processes have free frames
- **Global replacement**: Replace a page in any process
    - Issue: Page fault rate becomes uncontrollable

**Thrashing**: A process is busy swapping pages in and out, causing low CPU utilization

To determine the number of frames needed to avoid thrashing:

**Working Set**: Set of pages that a process is referencing in the near past

- based on principle of locality: temporal (recently accessed) and spatial (nearby pages)
- $\Delta$ = working set window = a fixed time interval or page reference count

**Prepaging**: Bring in multiple pages at once to reduce page faults. May cause I/O and memory contention.

## 9. File System

File: a contiguous logical address space for storing data

- **File handle**: A data structure that represents an open file
- **File descriptor**: An integer that identifies an open file within a process

Related data structures and resources:

- **File table** (per process): A list of all open files in the system, with their file handles and descriptors
- **Lock table**: A list of which files are locked by which processes
- **File cache**: A portion of memory used to store recently accessed file portions
- **I/O buffer**: A portion of memory used to store data being transferred between disk and memory

Access methods:

- **Sequential access**: Read from beginning to end
- **Direct access**: Read from any part of the file

**Directory**: A collection of nodes containing information about files. Each directory node corresponds to a file.

For each disk partition, there is a portion of the disk reserved for directory nodes before the data blocks.

### Directory Structure

Goals:

- To locate a file quickly
- Allow naming, protection, grouping

**Single-level directory**: A single directory for all users (Issue: naming, grouping)

**Two-level directory**: Each user has his own user file directory (UFD) in the master file directory (MFD) (Issue: grouping, sharing)

**Tree-structured directory**: Each directory can contain files and subdirectories (Issue: sharing)

**Acyclic-Graph directory**: Each directory can contain files, subdirectories, and links. No cycles allowed.

- **Dangling pointer**: A link that points to a deleted file (solution: back pointers / reference counters)
- **Soft link**: A pointer to a another pointer, which points to the file
- **Hard link**: A pointer to the file itself

**General Graph directory**: Allowing arbitary links between directories

- May cause cycles
- Solution: allow cycles, but use GC to reclaim disk space

**File System Mounting**: Attaching a file system to a directory

### Access Control

File sharing:

- Local file sharing done through a protection scheme (access control)
- Distributed file sharing done through a network file system
- Client-server model allows clients to mount remote file systems phsyically located on a server
- **NFS** for UNIX, **CIFS** for Windows

UNIX access control:

- 3 access modes: read (4), write (2), execute (1)
- 3 user types: owner, group, others

### File System Structure

**File System**: A collection of files and directories (on disk)

**File Control Block (FCB)**: Contains metadata about a file (e.g. Inode in UNIX)

**Device Driver**: Software that controls the physical device

Layers:

Application Program → Logical File System → File-Organization Module → Basic File System → I/O Control → Device

- Basic File System: Manages memory buffers and caches, signals the device driver
- File-organization module: Translates logical block numbers to physical block numbers, manages free space
- Logical File System: Manage metadata information

File system implementation:

- On-disk structure: Boot control block, volume control block, directory structure (per FS), FCB (per file)
- In-memory structure: System-wide open-file table, per-process open-file table

**Inode**: A data structure that denotes a file (or directory) in file systems

Implementation: Linear list, hash table, multi-level index

Allocation methods:

- Contiguous allocation: Allocate contiguous blocks to a file
    - A table stores `start` and `length` of each file
    - Advantages: Fast access; simple
    - Issue: External fragmentation; file size must be known in advance
- Linked allocation: Each block contains a pointer to the next block
    - Advantages: No external fragmentation; files can grow
    - Issue: Slow; no random access; pointer overhead
- Index allocation: Each file has a dedicated index block pointing to its data blocks
    - Advantages: Fast access; no external fragmentation; supports random access
    - Issue: pointer overhead

**File Allocation Table (FAT)**: A table that maps logical block numbers to physical block numbers

**Extent-based file system**: Allocate contiguous blocks in extents (logical file → extent → physical blocks)

### File System Performance

**Free Space Management**: Keep track of free blocks

**Bitmap**: use one bit for each block (1 if free, 0 if allocated)

- Advantages: Fast
- Issue: Space overhead
- For a disk of size $D$ and block size $B$, the bitmap size is $\frac{D}{B}$ bits

**Linked list**: each free block contains a pointer to the next free block

- Issue: cannot get contiguous blocks; slow access

**Grouping**: Group free blocks into groups of size $n$. Store the address of $n-1$ free blocks and a pointer to the next group, in the first free block.

**Counting**: Maintain a link of clusters in the format `(start, length)`

**Copy-on-write**: When a block is modified, instead of overwriting the block, copy the block to a new location and update the pointer

- Advantage: allow multiple access to the same file; no copies are created if the file is not modified

## 10. Storage Management

### Magnetic Disks

Electromagnetic storage device with rotating platters

- **Transfer rate**: Data transfer rate between disk and memory
- **Positioning time**:
    - **Seek time**: Time to move the disk arm to the desired track
    - **Rotational latency**: Time for the desired sector to rotate under the disk head
- **Head crash**: Disk head touches the disk surface, causing damage

Disk → Platter → Track → Sector

- Platter: a surface that stores data
- Track: a circular path with fixed radius on a platter
- Sector: a pie slice on a track
- Cylinder: set of all tracks with the same radius on all platters

Disk is addressed as a large array of **logical blocks**

**Network Attached Storage (NAS)**: Storage device connected to a network (NFS or CIFS)

**Storage Area Network (SAN)**: High-speed network that connects storage devices to servers

Storage → SAN → Server → Network → Client

**Disk formatting**: Divide disk into sectors that the disk controller can read/write

- Low-level formatting: Create tracks and sectors
- High-level formatting: Create file system

**Sector sparing**:

- Reserve some sectors for replacement
- After detecting a bad write, replace the sector with a spare sector and mark the bad sector as unusable

### Disk Scheduling

- **First Come First Serve (FCFS)**
- **Shortest Seek Time First (SSTF)**: Pick the closest request (may cause starvation)
- **SCAN**: Move disk arm in one direction, servicing requests along the way. Upon reaching the end, reverse direction.
    - **C-SCAN**: Move disk arm in one direction, servicing requests along the way. Upon reaching the end, move from the other end. (The disk is circular)
    - **C-LOOK**: Move disk arm in one direction, servicing requests along the way. Upon reaching the last request, reverse direction.

### Flash Memory

- NAND (for storage) and NOR (for code execution)
- **Solid State Drive (SSD)**: Flash memory with a controller

SSD → Flash memory → Block → Page → Cell

- Page: smallest unit of data that can be read/written
- Block: smallest unit of data that can be erased, consisting of multiple pages

Issues:

- Erase-before-write
- Random writes are slow
- Limited Program/Erase (P/E) cycles

**Flash Translation Layer (FTL)**: A firmware makes NAND flash behave like a disk

- Address translator: maps **logical block address (LBA)** to **physical block address (PBA)**
    - Page-level: each LBA maps to a PPA (issue: large mapping table)
    - Block-level: a range of LBAs maps to a PBA (issue: slow writes)
    - Hybrid:
        - **Data blocks** use block-level mapping for fast read
        - **Log blocks** use page-level mapping for fast write
        - When data blocks are updated, it will copy-on-write to log blocks
    - Demand-based: Instead of strong the complete mapping table in RAM,
        - Map of data pages are stored in translation pages on SSD
        - Translation pages are cached in RAM on demand
        - Map of translation pages (global translation map) is stored in RAM
        - VBA → Global Translation Table (RAM) → Translation Page (SSD or cached in RAM) → PBA → Data Block (SSD)
- Garbage collector: Reclaim pages occupied by out-place updates
    - Victim block selection
    - Live-page copying: Copy live pages to a new block
    - Victim block erasure
    - Victim block selection policies:
        - Random: Randomly select a block for long-term fairness
        - Round-robin: Select the next block in a round-robin fashion, for minimized P/E cycle difference
        - Greedy: Select the block with the most invalid pages for minimized live page copying
        - Cost-benefit: Select the block with the largest benefit-cost ratio for wear leveling
- Wear Leveling: Prolong the life of the SSD by distributing erases evenly across blocks
    - **Static wear leveling**: wear leveling across all blocks; proactively moving cold data to less-used blocks
    - **Dynamic wear leveling**: wear leveling across hot blocks
    - **Progressive wear leveling**: less wear leveling at the beginning of the SSD life
    - **Error-rate-aware wear leveling**: wear leveling based on error rate

**Bit Error Rate (BER)**: Portion of bits that are received incorrectly

Flash-aware file systems:

- Random writes are bad for flash memory (fragmentation, performance, wear)
- **Log-structured file system**: Write data sequentially to a log, then garbage collect
