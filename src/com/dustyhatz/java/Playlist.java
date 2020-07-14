// Example of using an ArrayList to create, and edit a desert island song playlist.
// By: Dustin Hatzenbuhler


import java.util.ArrayList;
import java.util.Collections;


class Playlist {

    public static void main(String[] args) {

        // Create and initialize the playlist
        ArrayList<String> desertIslandPlaylist = new ArrayList<String>();

        // Add songs to the playlist
        desertIslandPlaylist.add("Bittersweet Symphony");
        desertIslandPlaylist.add("Clair de Lune");
        desertIslandPlaylist.add("That's What You Get");
        desertIslandPlaylist.add("Punks and Poets");
        desertIslandPlaylist.add("Strangers");
        desertIslandPlaylist.add("Soulful");
        desertIslandPlaylist.add("When The End Comes");
        desertIslandPlaylist.add("Magic");
        desertIslandPlaylist.add("Can't Stop The Feeling");

        // Print the playlist and the size of the playlist
        System.out.println(desertIslandPlaylist);

        System.out.println("Size of playlist: " + desertIslandPlaylist.size());

        // Remove songs
        desertIslandPlaylist.remove("That's What You Get");
        desertIslandPlaylist.remove("Can't Stop The Feeling");
        desertIslandPlaylist.remove("When The End Comes");
        desertIslandPlaylist.remove("Punks and Poets");

        // Print the new size of the playlist
        System.out.println("Size of playlist after removal: " + desertIslandPlaylist.size());

        // Swap the first and second songs in the playlist
        Collections.swap(desertIslandPlaylist, 0, 1);
        
        // Print the final playlist
        System.out.println(desertIslandPlaylist);

    }
}