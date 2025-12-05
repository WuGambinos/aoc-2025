let () = print_endline "Hello, World!"


let () = 
    let lines = Advent.read_file "../day4_test.txt" in
    let _ = List.iter(fun x -> print_endline x) lines in
    ()
