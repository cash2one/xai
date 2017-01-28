

#calss header
class _SMART():
	def __init__(self,): 
		self.name = "SMART"
		self.definitions = [u'having a clean, tidy, and stylish appearance: ', u'A place or event that is smart attracts fashionable, stylish, or rich people: ', u'intelligent, or able to think quickly or intelligently in difficult situations: ', u'done quickly with a lot of force or effort: ', u'A smart machine, weapon, etc. uses computers to make it work so that it is able to act in an independent way: ', u'not showing respect, especially when making a funny remark: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
