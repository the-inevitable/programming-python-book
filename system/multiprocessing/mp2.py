"""
Use multiprocess anonymous pipes to communicate. Returns 2 connection
object representing ends of the pipe: objects are sent on one end and
received on the other, though pipes are bidirectional by default.
"""

from multiprocessing import Process, Pipe


def sender(pipe):
    """
    Send object to parent through anonymous pipe.
    :param pipe:
    :return:
    """
    msg = ['spam']
    msg.extend([42, 'eggs'])
    pipe.send(msg)
    pipe.close()


def talker(pipe):
    """
    Send and receive objects through a pipe.
    :param pipe:
    :return:
    """
    pipe.send({'name': 'Bob', 'spam': 42})
    reply = pipe.recv()
    print(f'talker got: {reply}')


if __name__ == '__main__':
    (parent_end, child_end) = Pipe()
    Process(target=sender, args=(child_end,)).start()
    print(f'parent got: {parent_end.recv()}')
    parent_end.close()

    (parent_end, child_end) = Pipe()
    child = Process(target=talker, args=(child_end,))
    child.start()
    print(f'parent got: {parent_end.recv()}')
    parent_end.send({x * 2 for x in 'spam'})
    child.join()
    print('Parent exit.')
