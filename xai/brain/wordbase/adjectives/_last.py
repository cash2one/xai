

#calss header
class _LAST():
	def __init__(self,): 
		self.name = "LAST"
		self.definitions = [u'(the person or thing) after everyone or everything else: ', u'finally: ', u'the least expected or wanted person or thing: ', u'at the latest time in the day: ', u'If you say that it is the last time you will do something, you mean that you will never do it again: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
