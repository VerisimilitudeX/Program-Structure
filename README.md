# Code Structure
* It is a way of organizing a program
* Code is organized into sections based on what is done, and its order
* For example: There is usually a starting section for importing libraries, declaring variables, etc.
  # Main Loop
  * A common section in a program is the main loop
  * It contains all the main interactions of the program
  * It keeps looping until the program is done
  * Loop is set up, then stays in it until it's ready for the program to end
  * Usually a while loop
  # Paragraph
  * Within each section of the program, code is also divided into paragraphs
  * Again like an essay
  * All on the same topic
  * Has no blank lines between code lines
  * Usually has one comment at top, explaining what it does
  * Can be fairly short
  * A way of grouping code together to make it more readable
  # Event Loop
  * A special paragraph that comes towards the top of the main loop
  * Usually the event loop is the first thing in the main loop
  * This loop lets code react to certain things that happen outside our program
  * Event loop is a type of loop; hence the colon (:)
  * This loop looks at something called events that happen while the code is running
  * This loop instructs the code to look at each event one at a time
  * For example:
    * for event in pygame.event.get():
    * if event.type == pygame.QUIT:
         * code that ends the main loop
    # Event
    * Things the event loop can react to
    * If something special happens, certain code will run
    * "In case of _____, do ______"
    * Events are usually caused by things that happen outside of the program
    * Events are different than other code because it can't be predicted when they'll occur
      # QUIT Events
      * QUIT event happens when user clicks the window close button
      * Code can written code that reacts to the QUIT event by ending the main loop to close the program
# Keep Pregram Open
* A computer program runs until it reaches the end of the code, then stops
* Usually, in a graphical program, the program runs until the user chooses to end it or for a really long time
* So in order to keep the program open, the code needs to be kept running
* To keep the code running, you can use a while loop
  * while drawing:
* Use a boolean variable to store whether the program should run or not
  * drawing = True
* The main loop draws a frame every time it runs
  * Draw and animate the frame
* In the main loop, use a conditional to check when the program should end
  * if program should end:
    * drawing = False
# Close Window
  * The most common way to end a program on a computer is letting the user close the window
  * In Pygame, the window has a built-in X button to let the user close it with the mouse
  * But the X button doesn't do anything unless it is coded to react
  * Even if the program ends based on another condition (like time), it's still good to let the user X it out in case of emergency
  * To activate the X button, we need to use the event loop
  * If the QUIT event is found, it is known that the user hit the close button
  * Then, the main loop can be ended by setting the loop boolean to False
# Paragraph Comments
* Paragraph comments aren't a technique that uses code; they're a technique to help our code
* It's important that we can read the code and find out what each part is supposed to do
* Paragraph comments are used to label a group of lines that work together to do one thing
* In other words, it is said what's going to happen (with the comment) before it is done (with the code)
* A paragraph comment is # ---, then the message, then --- #
* The message describes what the code below does
* Use paragraphs, with one comment before and line break after - it's faster and easier to read
# Summary
* Recall: Paragraphs are a way to organize code
* Makes code more readable at a glance
* Lines in a paragraph are related
* May do the same or similar tasks
* Comment at the top describes what paragraph does
* All lines here are related to setting up and executing this counting loop
* Comment could read # Print values 1 - 100 or similar
* Main loop is body of the program
* Keeps the program open until it's finished
* Event loop is usually towards the top of the main loop
* Event loop checks what events happened
* Main loop contains body of the program
* Main interactions: repeated input, drawing, animation, etc.
* Event loop reacts to events
* Contains code responding to: quit button, mouse, keyboard, etc.
