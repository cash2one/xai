

#calss header
class _OBSTINATE():
	def __init__(self,): 
		self.name = "OBSTINATE"
		self.definitions = [u'unreasonably determined, especially to act in a particular way and not to change at all, despite what anyone else says: ', u'used to describe a problem, situation, or thing that is difficult to deal with, remove, or defeat: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
