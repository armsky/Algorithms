
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
import threading


# Based on tornado.ioloop.IOLoop.instance() approach.
# See https://github.com/facebook/tornado
class SingletonMixin(object):
	__singleton_lock = threading.Lock()
	__singleton_instance = None

	@classmethod
	def instance(cls):
		if not cls.__singleton_instance:
			with cls.__singleton_lock:
				if not cls.__singleton_instance:
					cls.__singleton_instance = cls()
		return cls.__singleton_instance


if __name__ == '__main__':
	class A(SingletonMixin):
		pass

	class B(SingletonMixin):
		pass

	a, a2 = A.instance(), A.instance()
	b, b2 = B.instance(), B.instance()

	assert a is a2
	assert b is b2
	assert a is not b

	print('a:  %s\na2: %s' % (a, a2))
        print threading.current_thread()
	print('b:  %s\nb2: %s' % (b, b2))
        print threading.current_thread()
