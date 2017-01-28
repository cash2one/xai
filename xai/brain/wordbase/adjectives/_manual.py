

#calss header
class _MANUAL():
	def __init__(self,): 
		self.name = "MANUAL"
		self.definitions = [u'done with the hands: ', u'A manual machine is operated with the hands rather than by electricity or a motor: ', u'involving physical work rather than mental work: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
