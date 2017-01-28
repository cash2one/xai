

#calss header
class _GRUBBY():
	def __init__(self,): 
		self.name = "GRUBBY"
		self.definitions = [u'dirty: ', u"If you describe an activity or someone's behaviour as grubby, you do not think that it is honest, fair, or acceptable: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
