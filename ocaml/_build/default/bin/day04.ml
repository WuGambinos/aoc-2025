open Core

let () = Stdio.print_endline "Hello, World!"
let int_of_bool b = if b then 1 else 0

let check lines r c num_row num_col =
  if r >= num_row || r < 0
  then 0
  else if c >= num_col || c < 0
  then 0
  else (
    let row = List.nth_exn lines r in
    let cell = List.nth_exn row c in
    int_of_bool (Char.equal cell '@'))
;;

let string_to_char_list s =
  let len = String.length s in
  let rec loop i acc = if i < 0 then acc else loop (i - 1) (s.[i] :: acc) in
  loop (len - 1) []
;;

let convert_list string_list = List.map ~f:string_to_char_list string_list

let part1 lines =
  let num_row = List.length lines in
  let num_col = List.length (List.hd_exn lines) in
  let answer =
    List.foldi lines ~init:0 ~f:(fun r outer_acc row ->
      let acc =
        List.foldi row ~init:0 ~f:(fun c inner_acc item ->
          let x =
            if Char.equal item '@'
            then (
              let d1 = check lines (r - 1) c num_row num_col in
              let d2 = check lines (r + 1) c num_row num_col in
              let d3 = check lines r (c - 1) num_row num_col in
              let d4 = check lines r (c + 1) num_row num_col in
              let d5 = check lines (r + 1) (c + 1) num_row num_col in
              let d6 = check lines (r + 1) (c - 1) num_row num_col in
              let d7 = check lines (r - 1) (c + 1) num_row num_col in
              let d8 = check lines (r - 1) (c - 1) num_row num_col in
              let res = d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 in
              int_of_bool (res < 4))
            else 0
          in
          inner_acc + x)
      in
      outer_acc + acc)
  in
  answer |> string_of_int |> Stdio.print_endline;
  ()
;;

let () =
  let lines = Advent.read_file "../day4_input.txt" in
  let lines = List.map ~f:String.strip lines in
  let lines = convert_list lines in
  part1 lines;
  ()
;;
