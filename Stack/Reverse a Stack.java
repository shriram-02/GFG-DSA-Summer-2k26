class Solution {
    static void insertAtBottom(Stack<Integer> st, int x) {
        if (st.isEmpty()) {
            st.push(x);
            return;
        }
        int t = st.pop();
        insertAtBottom(st, x);
        st.push(t);
    }

    public static void reverseStack(Stack<Integer> st) {
        if (st.isEmpty()) return;
        int x = st.pop();
        reverseStack(st);
        insertAtBottom(st, x);
    }
}