type Person = {
  name: string,
  governmentId: string,
  email: string,
  debtAmount: number
  debtDueDate: string,
  debtId: string
}
const PersonDataComponent = ( person: Person ) => {
  return (
    <tr className="bg-white" key={person["debtId"]}>
      <td className="border px-4 py-2">{person.name}</td>
      <td className="border px-4 py-2">{person.governmentId}</td>
      <td className="border px-4 py-2">{person.email}</td>
      <td className="border px-4 py-2">{person.debtAmount}</td>
      <td className="border px-4 py-2">{person.debtDueDate}</td>
      <td className="border px-4 py-2">{person.debtId}</td>
    </tr>
  );
}

export {PersonDataComponent}