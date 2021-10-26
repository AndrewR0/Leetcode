class Solution {
    public int lengthOfLastWord(String s) {
        
        String newS = s.trim();

        for(int i = newS.length()-1; i >= 0; i--){
            //System.out.println(newS.charAt(i));
            if(newS.charAt(i) == ' '){
                System.out.println("if");
                return newS.substring(i+1).length();
            }
        }
        return newS.length();
    }
}