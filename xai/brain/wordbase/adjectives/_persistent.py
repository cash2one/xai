

#calss header
class _PERSISTENT():
	def __init__(self,): 
		self.name = "PERSISTENT"
		self.definitions = [u'lasting for a long time or difficult to get rid of: ', u'Someone who is persistent continues doing something or tries to do something in a determined but often unreasonable way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
