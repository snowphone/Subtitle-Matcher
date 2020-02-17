import { zip } from "../src/misc"


describe("zip function test", () => {
	it("tests zip function", () => {
		let lhs = [1, 2, 3, 4, 5, 6, 7],
			rhs = ["C", "D", 'E', 'F', 'G', 'A', 'B'],
			expected = [[1,'C'], [2, 'D'], [3, 'E'], [4, 'F'], [5, 'G'], [6, 'A'], [7, 'B']]
		expect(zip(lhs, rhs)).toEqual(expected)
	})

	it("tests with unbalanced arrays", () => {
		let lhs = [1, 2, 3, 4, 5, 6, 7],
			rhs = ["C", "D", 'E', 'F', 'G'],
			expected = [[1, 'C'], [2, 'D'], [3, 'E'], [4, 'F'], [5, 'G']]
		expect(zip(lhs, rhs)).toEqual(expected)
	})
})