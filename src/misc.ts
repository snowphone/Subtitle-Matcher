
export {zip}

function zip<T, R>(lhs: Array<T>, rhs: Array<R>): Array<[T, R]> {
	if (!lhs.length || !rhs.length) {
		return [];
	}
	return [[lhs[0], rhs[0]], ...zip(lhs.slice(1), rhs.slice(1))];
}

