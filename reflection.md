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

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
