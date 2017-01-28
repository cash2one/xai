

#calss header
class _LAX():
	def __init__(self,): 
		self.name = "LAX"
		self.definitions = [u'without much care, attention, or control: ', u'not severe or strong enough: ', u'(of a speech sound) made without much force']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
