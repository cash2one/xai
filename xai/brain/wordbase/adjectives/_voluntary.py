

#calss header
class _VOLUNTARY():
	def __init__(self,): 
		self.name = "VOLUNTARY"
		self.definitions = [u'done, made, or given willingly, without being forced or paid to do it: ', u'A voluntary organization is controlled and supported by people who give their time and money to it without being paid, and that exists to help other people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
