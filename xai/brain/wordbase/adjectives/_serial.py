

#calss header
class _SERIAL():
	def __init__(self,): 
		self.name = "SERIAL"
		self.definitions = [u'used to describe a person who repeatedly commits a similar crime or carries out a similar bad act, or the crime or act itself: ', u'broadcast or published in several separate parts, one after another: ', u'sending information one bit (= unit of information) at a time: ', u'arranged one after another: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
