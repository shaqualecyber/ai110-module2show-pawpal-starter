# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

When I first mapped out the project, I focused on what a pet owner would actually need to accomplish during a typical day. I identified three core actions that would drive the design: keeping track of pet information, managing care activities, and creating a daily plan that fits the owner's schedule. Those actions guided my initial UML design.

To support those features, I created four classes with separate responsibilities. The PetProfile class stores information about the pet, including details that could affect its daily care. The CareActivity class represents individual care activities, such as walks, meals, medication, grooming, or enrichment. The OwnerProfile class stores the owner's available time and care preferences so the schedule can be built around their routine. Finally, the SchedulePlanner class is responsible for organizing care activities into a daily schedule based on the owner's available time and the priority of each activity.


**b. Design changes**

During the review of my class skeleton, I made a couple of small design improvements based on AI feedback. I updated the naming so that both OwnerProfile and SchedulePlanner consistently use available_minutes, which makes the code easier to understand and keeps the naming consistent across the project. I also updated the activity_list type hint to specify that it stores CareActivity objects instead of using a generic list. I chose not to add additional object relationships at this stage because the assignment focused on creating class skeletons rather than implementing the application's behavior.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

My scheduler considers the owner's available time, the priority level of each care activity, whether a task has already been completed, and any due dates used for recurring tasks or conflict detection. I decided that available time and task priority were the most important constraints because a pet owner may not always have enough time to complete every activity. In those situations, the scheduler makes sure the highest-priority tasks are completed first while identifying any tasks that had to be skipped.

**b. Tradeoffs**

One decision I made was to keep the conflict detection simple. Right now, it only checks if two tasks are scheduled for the exact same due date or time instead of looking for activities that overlap. I could have used a more advanced approach that groups activities or checks time ranges, which would be more efficient as the project grows. I decided to stick with the simpler version because it's easier to read, easier to follow, and fits the size of this project while still meeting the requirements.

---

## 3. AI Collaboration

**a. How you used AI**

I used my AI coding assistant throughout the project to help brainstorm ideas, review my code, explain Python concepts, generate unit tests, debug issues, and improve my documentation. The features I found most helpful were having the AI review my existing code, explain why certain changes were recommended, and verify that my implementation matched the requirements for each phase instead of simply generating new code. Using separate chat sessions for each phase also helped me stay organized because every conversation focused on one part of the project. That made it much easier to go back and review previous work without having unrelated topics mixed together.

**b. Judgment and verification**

One example of where I chose not to accept an AI suggestion exactly as it was written was during the README updates. The AI suggested making additional formatting changes beyond what the assignment required, but I decided to keep the documentation focused on the required sections and only removed a duplicate heading to improve readability. Throughout the project, I reviewed every suggestion before accepting it, ran my automated tests, compared the results to the project requirements, and verified the program output to make sure the changes worked as expected.

---

## 4. Testing and Verification

**a. What you tested**

I created automated tests for the main scheduling behaviors, including marking activities as completed, adding activities to a pet, sorting activities by estimated time, filtering completed and pending tasks, recurring daily and weekly activities, conflict detection, and schedule generation when time was limited. These tests helped verify that the scheduler behaved correctly under different conditions and reduced the chance of introducing bugs as I added new features.

**b. Confidence**

I'm very confident that my scheduler works as expected because all 14 automated tests passed successfully, and I also verified the application's behavior by running main.py and reviewing the output. If I had more time, I would add additional tests for larger schedules with multiple pets, overlapping activity times, and more complex recurring scheduling scenarios.

---

## 5. Reflection

**a. What went well**

The part of the project I'm most satisfied with is seeing everything come together into a working application. It was rewarding to start with a simple UML diagram and gradually build a scheduler that can prioritize activities, detect conflicts, handle recurring tasks, filter completed activities, and explain why the schedule was created the way it was.

**b. What you would improve**

If I continued working on this project, I would improve the conflict detection so it could identify overlapping activities instead of only matching identical due times. I'd also expand the Streamlit interface by allowing users to edit or delete existing activities and provide additional scheduling preferences to make the planner more flexible.

**c. Key takeaway**

One of the biggest things I learned from this project is what it means to be the "lead architect" when working with AI. AI was a valuable tool for explaining concepts, generating ideas, and speeding up parts of the development process, but I was still responsible for making the final design decisions. I learned that good AI-assisted development isn't about accepting every suggestion. It's about reviewing recommendations, testing the results, and making sure the final solution matches the project requirements and my overall design.
