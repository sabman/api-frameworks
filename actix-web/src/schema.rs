table! {
    test_frameworks (id) {
        id -> Int4,
        test_data -> Varchar,
    }
}

table! {
    users (id) {
        id -> Varchar,
        name -> Varchar,
    }
}

allow_tables_to_appear_in_same_query!(
    test_frameworks,
    users,
);
