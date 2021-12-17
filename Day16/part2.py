import math


def convert_hex_packet_to_binary(packet: str) -> str:
    return "".join([f"{int(c, 16):>04b}" for c in packet])


def decode_packet(
    packet: str, packets: list[int, int, int], numbers: list[int]
) -> tuple[str, list[int, int, int], list[int], int]:

    literal_value = 0
    version: int = int(packet[:3], 2)

    if int(packet, 2) == 0:
        return (packet, packets)
    type_id: int = int(packet[3:6], 2)
    pos: int = 6

    if type_id == 4:  # literal value
        bit_groups: list[str] = []
        while True:
            bit_groups.append(packet[pos + 1 : pos + 5])
            if packet[pos] == "0":
                pos += 5
                break
            pos += 5

        literal_value = int("".join(bit_groups), 2)
        numbers.append(literal_value)
        packet = packet[pos:]
    else:  # operator
        length_type_id = int(packet[6:7])
        pos += 1
        sub_numbers = []
        if length_type_id:
            num_sub_packets = int(packet[7:18], 2)
            pos += 11
            packet = packet[pos:]
            for _ in range(num_sub_packets):
                packet, packets, sub_numbers = decode_packet(
                    packet, packets, sub_numbers
                )

                if not packet:
                    break

        else:
            total_length_in_bits = int(packet[7:22], 2)
            pos += 15
            packet = packet[pos:]
            packet_length = len(packet)
            # need to check length of packet
            while packet and len(packet) + total_length_in_bits > packet_length:
                packet, packets, sub_numbers = decode_packet(
                    packet, packets, sub_numbers
                )

        numbers.append(calculate_expression(type_id, sub_numbers))

    packets.append([version, type_id, numbers])
    return (packet, packets, numbers)


def calculate_expression(type_id: int, numbers: list[int]) -> int:
    calculation = 0
    if type_id == 0:
        calculation += sum(numbers)
    elif type_id == 1:
        calculation += math.prod(numbers)
    elif type_id == 2:
        calculation += min(numbers)
    elif type_id == 3:
        calculation += max(numbers)
    elif type_id == 5:
        calculation += int(numbers[0] > numbers[1])
    elif type_id == 6:
        calculation += int(numbers[0] < numbers[1])
    elif type_id == 7:
        calculation = int(numbers[0] == numbers[1])

    return calculation


def decode_transmission(binary_packet: str) -> str:
    packet, packets, numbers = decode_packet(binary_packet, [], [])
    return numbers[0]


def main() -> None:
    with open("Day16/input.txt") as f:
        packet = f.readline().rstrip()

    binary_packet: str = convert_hex_packet_to_binary(packet)

    calculation = decode_transmission(binary_packet)

    print(f"Calculation: {calculation}")


if __name__ == "__main__":
    main()
