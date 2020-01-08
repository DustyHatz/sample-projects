package com.dustyhatz;

public class Madlibs {
    /*
    This program generates a mad libbed story.
    Author: Dustin Hatzenbuhler
    Date: 9/4/2019
    */
    public static void main(String[] args) {

        String name1 = "Dustin";
        String name2 = "Cash";
        String adjective1 = "slimy";
        String adjective2 = "black";
        String adjective3 = "crunchy";
        String verb1 = "terminate";
        String noun1 = "ball";
        String noun2 = "butt";
        String noun3 = "eye";
        String noun4 = "couch";
        String noun5 = "TV";
        String noun6 = "dog";
        int number = 37;
        String place1 = "Ireland";


        String story = "This morning " + name1 + " woke up feeling " + adjective1 + ". 'It is going to be a " + adjective2 + " day!' Outside, a bunch of " + noun1 + "s were protesting to keep " + noun2 + " in stores. They began to " + verb1 + " to the rhythm of the " + noun3 + ", which made all the " + noun4 + "s very " + adjective3 + ". Concerned, " + name1 + " texted " + name2 + ", who flew " + name1 + " to " + place1 + " and dropped " + name1 + " in a puddle of frozen " + noun5 + ". " + name1 + " woke up in the year " + number + ", in a world where " + noun6 + "s ruled the world.";
        System.out.println(story);
    }
}