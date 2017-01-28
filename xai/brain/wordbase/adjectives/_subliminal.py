

#calss header
class _SUBLIMINAL():
	def __init__(self,): 
		self.name = "SUBLIMINAL"
		self.definitions = [u'not recognized or understood by the conscious mind, but still having an influence on it: ', u'Subliminal advertising tries to influence people without them being aware of it, for example by showing messages for such a short time that people read them without realizing that they have done so.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
