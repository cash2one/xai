

#calss header
class _DUE():
	def __init__(self,): 
		self.name = "DUE"
		self.definitions = [u'expected to happen, arrive, etc. at a particular time: ', u'at a suitable time in the future: ', u'because of: ', u'owed as a debt or as a right: ', u'If you are due for something, you expect to receive it, because you deserve it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
