class Solution {
    void sortedInsert(Stack<Integer> st, int x) {
        if (st.isEmpty() || st.peek() <= x) {
            st.push(x);
            return;
        }
        int t = st.pop();
        sortedInsert(st, x);
        st.push(t);
    }

    public void sortStack(Stack<Integer> st) {
        if (st.isEmpty()) return;
        int x = st.pop();
        sortStack(st);
        sortedInsert(st, x);
    }
}