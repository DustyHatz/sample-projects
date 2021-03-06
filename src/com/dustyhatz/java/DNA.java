// Example program using basic conditionals to identify
// whether a protein exists in a strand of DNA

package com.dustyhatz;
import java.util.Scanner;


public class Main {

    public static void main(String[] args) {

        // Get DNA strand from input
        // Example "ATTAATATGTACTGA"
        String dna;

        Scanner input = new Scanner(System.in);

        System.out.println("Enter DNA: ");

        dna = input.nextLine();

        // Find and print the length of the DNA strand
        System.out.println("Length: " + dna.length());

        // Find and print the start codon
        int start = dna.indexOf("ATG");

        System.out.println("Start: " + start);

        // Find and print the stop codon
        int stop = dna.indexOf("TGA");

        System.out.println("Stop: " + stop);

        // Check that start and stop codons exist
        if (start != -1 && stop != -1) {

            System.out.println("Condition 1 and 2 are satisfied.");
        }

        // Check that each additional codon is a sequence of 3 nucleotides
        if (start != -1 && stop != -1 && (stop - start) % 3 == 0) {

            System.out.println("Condition 1, 2, and 3 are satisfied.");

            // Identify and print the protein
            String protein = dna.substring(start, stop + 3);

            System.out.println("Protein: " + protein);

        // If there are no protein codons print No Protein detected
        } else {

            System.out.println("No protein detected.");
        }
    }
}
