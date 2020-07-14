
// Example of using variables and concatenating strings to generate a "MadLib" story.
// Author: Dustin Hatzenbuhler


package com.dustyhatz;

public class Madlibs {

    public static void main(String[] args) {

        // Create example variables to be used in story
        // Two names
        String name1 = "Dustin";
        String name2 = "Cash";

        // Three adjectives
        String adjective1 = "slimy";
        String adjective2 = "black";
        String adjective3 = "crunchy";

        // One verb
        String verb1 = "terminate";

        // Six nouns
        String noun1 = "ball";
        String noun2 = "butt";
        String noun3 = "eye";
        String noun4 = "couch";
        String noun5 = "TV";
        String noun6 = "dog";

        // One number
        int number = 37;

        // One place
        String place1 = "Ireland";

        // Create story by concatenating the variables with the story string and print
        String story = "This morning " + name1 + " woke up feeling " + adjective1 + ". 'It is going to be a " + adjective2 + " day!' Outside, a bunch of " + noun1 + "s were protesting to keep " + noun2 + " in stores. They began to " + verb1 + " to the rhythm of the " + noun3 + ", which made all the " + noun4 + "s very " + adjective3 + ". Concerned, " + name1 + " texted " + name2 + ", who flew " + name1 + " to " + place1 + " and dropped " + name1 + " in a puddle of frozen " + noun5 + ". " + name1 + " woke up in the year " + number + ", in a world where " + noun6 + "s ruled the world.";
        
        System.out.println(story);
    }
}