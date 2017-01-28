

#calss header
class _LAME():
	def __init__(self,): 
		self.name = "LAME"
		self.definitions = [u'(especially of animals) not able to walk correctly because of physical injury to or weakness in the legs or feet', u'(especially of an excuse or argument) weak and unsatisfactory: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
